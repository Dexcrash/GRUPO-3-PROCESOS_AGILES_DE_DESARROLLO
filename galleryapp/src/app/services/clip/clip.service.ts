import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { MessageService } from '../message/message.service';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Clip } from './clip';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})

export class ClipService {

  API_URL = 'http://localhost:8000/clips';
  private clips: Array<Clip> = [];

  constructor(
    private messageService: MessageService,
    private httpClient: HttpClient
  ) { }

  getClips(media_id: number): Observable<Clip[]> {
    this.messageService.add('ClipService: fetched clips');
    let params = new HttpParams();
    params = params.append('media_id', media_id.toString());

    this.httpClient.get(this.API_URL, {params}).subscribe((data: Array<any>) => {
      data.forEach(dataItem => {
        var p = JSON.stringify(dataItem.fields)
        let clp = JSON.parse(p);
        this.clips.push(clp)
      });
    });
    return of(this.clips);
  }


  getMultimedia(id: number): Observable<Clip> {
    this.messageService.add(`ClipService: fetched multimedia id=${id}`);
    return of(this.clips.find(clip => clip.id === id));  
  }

  clearClip(){
    this.clips = [];
  }

  addClip(id_usuario: number, id_multimedia: number, nombre: String, segundo_inicio: number, segundo_fin: number): Observable<any> {
    this.messageService.add('RegisterService: Login call');
    var obj = { usuario: id_usuario, nombre: nombre, multimedia: id_multimedia, segundoInicio: segundo_inicio, segundoFin: segundo_fin}
    this.httpClient.post(this.API_URL, JSON.stringify(obj), httpOptions).subscribe((data: Response) => {
      if (data[0].fields.nombre == nombre) {
        this.messageService.add('Clip adicionado');
        this.messageService.authenticate(true);
      } else {
        this.messageService.add('Clip incorrecto');
        this.messageService.authenticate(false);
      }
    });
    return of(obj);
  }


}
