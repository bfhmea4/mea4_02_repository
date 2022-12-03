import { Component, OnInit } from '@angular/core';
import {FilerepoService} from "../filerepo.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-activitylist',
  templateUrl: './activitylist.component.html',
  styleUrls: ['./activitylist.component.css']
})
export class ActivitylistComponent implements OnInit {

  listActivities: any;
  loading: boolean = false;
  activity: any;
  file: any;


  constructor(private fileService: FilerepoService, private route: ActivatedRoute) {
  }

  ngOnInit(): void {
    let activityList = this.fileService.getActivityList();

    this.fileService.getActivityList().forEach((entry) => this.listActivities = entry);
  }

  onchange(event: any){
    this.activity = event.target.files[0];
  }

  uploadFile(){
    this.loading = !this.loading;
        let formData: any = new FormData()
        formData.append("activity", this.activity);
        this.fileService.uploadFile(formData).subscribe(
      (res) => {
        this.ngOnInit()
      },
      (err) => console.log(err)
    );
    }
}
