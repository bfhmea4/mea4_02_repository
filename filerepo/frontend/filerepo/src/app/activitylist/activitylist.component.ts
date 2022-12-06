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
  activityList: any;
  activityListToPrint: any = [];

  constructor(private fileService: FilerepoService, private route: ActivatedRoute, private uploadActivityService: UploadActivityService ) {
  }

  async ngOnInit(): Promise<void> {
    this.activityListToPrint = []
    await this.uploadActivityService.getUploadActivity().forEach((entry) => { this.activityList=entry});
    this.activityList = this.activityList.sort((n1: { upload_time: number; }, n2: { upload_time: number; }) =>
      n2.upload_time - n1.upload_time
    );

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
