import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {FilerepoService} from "../filerepo.service";
import {UploadActivityService} from "../fi";
import {File} from "../file";
import {empty} from "rxjs";

class UploadActivity {
}

@Component({
  selector: 'app-fileinfo',
  templateUrl: './fileinfo.component.html',
  styleUrls: ['./fileinfo.component.css']
})
export class FileinfoComponent implements OnInit {
  file: File;
  upload_activity: UploadActivity;
  creation_time: Date=new Date(0);
  update_time: Date=new Date(0);
  id: any;

  constructor(private fileService: FilerepoService, private route: ActivatedRoute, private ) {
    this.file = <File>{};
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
    })
    this.fileService.getFileInfo(this.id).subscribe((data: File) => {
      this.file = data
      this.creation_time=new Date(this.file.file_creation_time*1000);
      this.update_time=new Date(this.file.file_update_time*1000);
    })
  }
  downloadContent(url: string){
    console.log(url);
    window.open(url);
  }
  deleteFile(id: string){
    console.log(id);
    this.fileService.deleteFile(id).subscribe(data =>{
      console.log(data)
      window.location.assign("/")
    });
  }

}
