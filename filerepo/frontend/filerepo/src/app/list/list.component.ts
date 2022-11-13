import { Component, OnInit } from '@angular/core';
import {AppRoutingModule} from "../app-routing.module";
import {ServiceService} from "../service.service";

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})




export class ListComponent implements OnInit {
  listFiles: any;
  loading: boolean = false;
  file: any;


  constructor(private fileService: ServiceService, private route: AppRoutingModule) {
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
