import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {FilerepoService} from "../filerepo.service";
import {File} from "../file";
import {empty} from "rxjs";

@Component({
  selector: 'app-fileinfo',
  templateUrl: './fileinfo.component.html',
  styleUrls: ['./fileinfo.component.css']
})
export class FileinfoComponent implements OnInit {
  file: File;
  id: string;

  constructor(private api: FilerepoService, private route: ActivatedRoute) {
    this.file = <File>{};
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      console.log(params);
      this.id = params.get('id');
    })
    this.file=this.api.getFileInfo(this.id)
  }

}
