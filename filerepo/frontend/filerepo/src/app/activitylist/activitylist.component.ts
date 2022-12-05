import { Component, OnInit } from '@angular/core';
import {FilerepoService} from "../filerepo.service";
import {ActivatedRoute} from "@angular/router";
import {UploadActivityService} from "../filerepo.service";
import {File} from "../file";
import {UploadActivity} from "../uploadActivity";
import {empty} from "rxjs";


@Component({
  selector: 'app-activitylist',
  templateUrl: './activitylist.component.html',
  styleUrls: ['./activitylist.component.css']
})
export class ActivitylistComponent implements OnInit {
  file: File;
  loading: boolean = false;
  upload_activity: UploadActivity;
  id: any;
  activityList: any;
  listFiles: any;


  constructor(private fileService: FilerepoService, private route: ActivatedRoute, private uploadActivityService: UploadActivityService ) {
    this.file = <File>{};
    this.upload_activity = <UploadActivity>{};
  }

  ngOnInit(): void {

    let activityList = this.uploadActivityService.getUploadActivity();
    // activityList.forEach((entry) => this.upload_activity = entry);
    this.fileService.getFileList().forEach((entry) => this.listFiles = entry);
  }

  onchange(event: any){
    // this.upload_activity = event.target.activityList[0];
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
