import { Injectable } from '@angular/core';
import { Image } from './image';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ImageService {
  API_URL = 'http://localhost:8000';
  private images: Array<Image> = [];

  constructor(private messageService: MessageService,
    private httpClient: HttpClient
  ) { }

  getImages(): Observable<Image[]> {
    this.messageService.add('ImageService: fetched images');
    this.images = [];
    this.httpClient.get(`${this.API_URL}/`).subscribe((data: Array<any>) => {
      data.forEach(dataItem => {
        let image1 = new Image();
        image1.id = dataItem.pk;
        image1.name = dataItem.fields.titulo;
        image1.url = dataItem.fields.url;
        image1.description = dataItem.fields.info;
        image1.imageFile = dataItem.fields.archivo;
        image1.type = dataItem.fields.tipo;
        image1.autor = dataItem.fields.autor;
        image1.ciudad = dataItem.fields.ciudad;
        image1.pais = dataItem.fields.pais;
        image1.fecha_creacion = dataItem.fields.fecha_creacion;
        this.images.push(image1)
      });
    });
    return of(this.images);
  }


  getImage(id: number): Observable<Image> {
    this.messageService.add(`ImageService: fetched image id=${id}`);
    return of(this.images.find(image => image.id === id));  
  }


}
