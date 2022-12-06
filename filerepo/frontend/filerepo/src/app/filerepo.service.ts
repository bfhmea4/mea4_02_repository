import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { File } from "./file";
import {UploadActivity} from "./uploadActivity";

const localUrl = 'http://127.0.0.1:8000/files';
const localUrlUploadActivity = 'http://127.0.0.1:8000/uploadactivities';

@Injectable({
  providedIn: 'root'
})
export class FilerepoService {

  constructor(private http: HttpClient) {
  }

  public getFileInfo(id: string){
    return this.http.get<File>(localUrl + "/"+id+"/info");
  }
  public deleteFile(id: string){
    return this.http.delete(localUrl + "/"+id);
  }

  public getFileList(){
    return this.http.get<File>(localUrl + "/")
  }

  public uploadFile(formData: FormData){
    return this.http.post<any>(localUrl + "/upload", formData)
  }
}

@Injectable({
  providedIn: 'root'
})
export class UploadActivityService {

  constructor(private http: HttpClient) {
  }

    public getUploadActivityByID(id: string){
    return this.http.get<UploadActivity>(localUrlUploadActivity + "/"+id);
  }

  public getUploadActivity(){
    return this.http.get<UploadActivity>(localUrlUploadActivity);
  }
}
