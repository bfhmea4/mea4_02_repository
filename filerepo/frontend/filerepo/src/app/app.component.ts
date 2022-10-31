
import { Component, OnInit } from '@angular/core';
import { FilerepoService } from './filerepo.service';
import {ActivatedRoute} from "@angular/router";
import {File_list} from "./file_list";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent{
  title = 'filerepo';

}
