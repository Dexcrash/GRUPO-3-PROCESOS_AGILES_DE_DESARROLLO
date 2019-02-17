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

  API_URL = 'http://localhost:8000/get_clips';
  private clips: Array<Clip> = [];

  constructor(
    private messageService: MessageService,
    private httpClient: HttpClient
  ) { 

  }

  getClips(media_id: number): Observable<Clip[]> {
    this.messageService.add('ClipService: fetched clips');
    this.clips = [];
    var obj = { media_id : media_id}

    this.httpClient.get(this.API_URL, httpOptions).subscribe((data: Array<any>) => {
      data.forEach(dataItem => {
        let cl = new Clip();
        cl.id = dataItem.pk;
        cl.nombre = dataItem.fields.titulo;
        cl.usuario_id = dataItem.fields.usuario;
        cl.multimedia_id = dataItem.fields.multimedia_id;
        cl.segundo_inicio = dataItem.fields.segundo_inicio;
        cl.segundo_fin = dataItem.fields.segundo_fin;
        this.clips.push(cl)
      });
    });
    return of(this.clips);
  }


  getMultimedia(id: number): Observable<Clip> {
    this.messageService.add(`ClipService: fetched multimedia id=${id}`);
    return of(this.clips.find(clip => clip.id === id));  
  }


}
