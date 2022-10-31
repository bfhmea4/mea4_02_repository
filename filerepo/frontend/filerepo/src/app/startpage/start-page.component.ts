import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {FilerepoService} from "../filerepo.service";
import {File} from "../file";
import {File_list} from "../file_list";
import * as events from "events";



@Component({
  selector: 'app-fileinfo',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.css']
})
export class StartPageComponent implements OnInit{
  listFiles: File_list[];
  file: File;


  constructor(private fileService: FilerepoService, private route: ActivatedRoute) {
    this.listFiles = [<File_list>{}];
  }

  ngOnInit(): void {
        this.fileService.getFileList().forEach((entry: File) => this.listFiles.push({
          id: entry.id,
          file_name: entry.file_name,
        }))
  }


  uploadFile(){
        this.fileService.uploadFile(this.file).subscribe(
            (event: any) => {
                if (typeof (event) === 'object') {
                    this.file = event.file
                }
            }
        );
  }
}





