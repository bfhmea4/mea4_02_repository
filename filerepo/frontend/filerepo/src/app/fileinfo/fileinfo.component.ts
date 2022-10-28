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
  id: any;

  constructor(private fileService: FilerepoService, private route: ActivatedRoute) {
    this.file = <File>{};
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      this.id = params.get('id');
    })
    this.fileService.getFileInfo(this.id).subscribe((data: File) => this.file = data)
  }

}
