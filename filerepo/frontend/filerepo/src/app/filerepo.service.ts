import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { File } from "./file";

const localUrl = 'http://127.0.0.1:8000/files';
@Injectable({
  providedIn: 'root'
})
export class FilerepoService {

  constructor(private http: HttpClient) {
  }

  public getFileInfo(id: string){
    return this.http.get<File>(localUrl + "/"+id+"/info")
  }
}
