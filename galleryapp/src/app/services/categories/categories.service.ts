import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { MessageService } from '../message/message.service';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Router } from '@angular/router';
import { Category } from './category.model'

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})

export class CategoriesService {

  API_URL = 'http://localhost:8000/api/categorias';
  private categories: Array<Category> = [];

  constructor(
    private messageService: MessageService,
    private httpClient: HttpClient,
    private router: Router
  ) { }

  getCategories(): Observable<Category[]> {
    this.categories  = [];
    this.messageService.add('CategoryService: fetched categories');
    this.httpClient.get(this.API_URL).subscribe((data: Array<any>) => {
      data.forEach(dataItem => {
        var cat = new Category();
        cat.id = dataItem.pk;
        cat.name = dataItem.fields.nombre
        this.categories.push(cat)
      });
    });
    return of(this.categories);
  }
}
