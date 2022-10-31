import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {FilerepoService} from "../filerepo.service";
import {File} from "../file";
import {File_list} from "../file_list";

@Component({
  selector: 'app-fileinfo',
  templateUrl: './startpage.component.html',
  styleUrls: ['./startpage.component.css']
})
export class StartpageComponent implements OnInit{
  listFiles: File_list;
  private function_upload(): void{
    this.fileService.
  }

  constructor(private fileService: FilerepoService, private route: ActivatedRoute) {
    this.listFiles = <File_list>{};
  }

  ngOnInit(): void {
        this.fileService.getFileList().forEach((entry: File_list) => this.listFiles = {
          id: entry.id,
          file_name: entry.file_name,
        })
    }


    e = document.getElementById("button").addEventListener("click", this.function_upload)

}





