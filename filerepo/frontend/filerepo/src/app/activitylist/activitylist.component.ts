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
  file: any;
  loading: boolean = false;
  upload_activity: any;
  activityList: any;
  activityListToPrint: any = [];
  listFiles: any;


  constructor(private fileService: FilerepoService, private route: ActivatedRoute, private uploadActivityService: UploadActivityService ) {
  }

  async ngOnInit(): Promise<void> {
    this.activityListToPrint = []
    await this.uploadActivityService.getUploadActivity().forEach((entry) => { this.activityList=entry});

    this.activityList.forEach((entry: any) => {
      let newEntry = {
        file_id: entry.file_id,
        file_name: entry.file_name,
        upload_time: new Date(entry.upload_time*1000).toTimeString(),
      }
    this.activityListToPrint.push(newEntry)
    })
  }

  onchange(event: any){
    //this.upload_activity = event.target.upload_activity[0];
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
