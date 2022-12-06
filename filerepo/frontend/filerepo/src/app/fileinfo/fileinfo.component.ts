import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {FilerepoService} from "../filerepo.service";
import {UploadActivityService} from "../filerepo.service";
import {File} from "../file";
import {UploadActivity} from "../uploadActivity";
import {empty} from "rxjs";


@Component({
  selector: 'app-fileinfo',
  templateUrl: './fileinfo.component.html',
  styleUrls: ['./fileinfo.component.css']
})
export class FileinfoComponent implements OnInit {
  file: File;
  creation_time: Date=new Date(0);
  update_time: Date=new Date(0);
  activityList: any;
  activityListToPrint: any = [];
  id: any;

  constructor(private fileService: FilerepoService, private route: ActivatedRoute, private uploadActivityService: UploadActivityService ) {
    this.file = <File>{};
  }

  async ngOnInit(): Promise<void> {
    this.activityListToPrint = []
    await this.uploadActivityService.getUploadActivity().forEach((entry) => {
      this.activityList = entry
    });
    this.activityList.forEach((entry: any) => {
      let newEntry = {
        file_id: entry.file_id,
        file_name: entry.file_name,
        upload_time: new Date(entry.upload_time * 1000).toTimeString(),
      }
      this.activityListToPrint.push(newEntry)
    })



    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
    })
    this.fileService.getFileInfo(this.id).subscribe((data: File) => {
      this.file = data
      this.creation_time = new Date(this.file.file_creation_time * 1000);
      this.update_time = new Date(this.file.file_update_time * 1000);
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
