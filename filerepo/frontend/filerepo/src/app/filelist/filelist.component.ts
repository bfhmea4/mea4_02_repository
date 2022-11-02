import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import {FilerepoService} from "../filerepo.service";

@Component({
  selector: 'app-filelist',
  templateUrl: './filelist.component.html',
  styleUrls: ['./filelist.component.css']
})
export class FilelistComponent implements OnInit {
  listFiles: any;
  loading: boolean = false;
  file: any;


  constructor(private fileService: FilerepoService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.fileService.getFileList().forEach((entry) => this.listFiles = entry);
  }

  onchange(event: any){
    this.file = event.target.files[0];
  }

  uploadFile(){
    this.loading = !this.loading;
        let formData: any = new FormData()
        formData.append("file", this.file);
        this.fileService.uploadFile(formData).subscribe(
      (res) => {
        this.ngOnInit()
      },
      (err) => console.log(err)
    );
    }
}
