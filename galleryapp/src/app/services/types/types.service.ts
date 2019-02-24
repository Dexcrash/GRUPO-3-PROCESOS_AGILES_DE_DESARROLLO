import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { MessageService } from '../message/message.service';
import { HttpClient } from '@angular/common/http';
import { Type } from './type.model'


@Injectable({
  providedIn: 'root'
})
export class TypesService {
  API_URL = 'http://localhost:8000/api/tipos';
  private types: Array<Type> = [];

  constructor(
    private messageService: MessageService,
    private httpClient: HttpClient
  ) { }

  getTypes(): Observable<Type[]> {
    this.messageService.add('TypeService: fetched types');
    this.types = [];
    this.httpClient.get(this.API_URL).subscribe((data: Array<any>) => {
      data.forEach(dataItem => {
        let tp = new Type();
        tp.id = dataItem.pk;
        tp.name = dataItem.fields.tipo;
        this.types.push(tp)
      });
    });
    return of(this.types);
  }
}
