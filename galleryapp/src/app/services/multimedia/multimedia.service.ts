import { Injectable } from '@angular/core';
import { Multimedia } from './multimedia';
import { Observable, of } from 'rxjs';
import { MessageService } from '../message/message.service';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class MultimediaService {
  API_URL = 'http://localhost:8000/';
  private multimedias: Array<Multimedia> = [];

  constructor(
    private messageService: MessageService,
    private httpClient: HttpClient
  ) { }

  getMultimedias(): Observable<Multimedia[]> {
    this.messageService.add('MultimediaService: fetched images');
    this.multimedias = [];
    this.httpClient.get(this.API_URL).subscribe((data: Array<any>) => {
      data.forEach(dataItem => {
        let mu = new Multimedia();
        mu.id = dataItem.pk;
        mu.name = dataItem.fields.titulo;
        mu.url = dataItem.fields.url;
        mu.description = dataItem.fields.info;
        mu.imageFile = dataItem.fields.archivo;
        mu.type = dataItem.fields.tipo;
        mu.autor = dataItem.fields.autor;
        mu.ciudad = dataItem.fields.ciudad;
        mu.pais = dataItem.fields.pais;
        mu.fecha_creacion = dataItem.fields.fecha_creacion;
        this.multimedias.push(mu)
      });
    });
    return of(this.multimedias);
  }


  getMultimedia(id: number): Observable<Multimedia> {
    this.messageService.add(`MultimediaService: fetched multimedia id=${id}`);
    return of(this.multimedias.find(multimedia => multimedia.id === id));  
  }


}
