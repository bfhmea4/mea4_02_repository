
import { Component, OnInit } from '@angular/core';
import { FilerepoService } from './filerepo.service';
import {ActivatedRoute} from "@angular/router";
import {File_list} from "./file_list";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit{
  title = 'filerepo';
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
