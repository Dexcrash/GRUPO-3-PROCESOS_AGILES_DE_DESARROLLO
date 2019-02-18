import { Injectable } from '@angular/core';
import { Observable, of, pairs } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { MessageService } from '../message/message.service';
import { Router } from '@angular/router';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};


@Injectable({
  providedIn: 'root'
})
export class EditService {

  API_URL = 'http://localhost:8000/signup';

  constructor(private messageService: MessageService,
    private httpClient: HttpClient,
    private router: Router) { 

    }


  edit( first_name: String, last_name: String, email: String, pais: String, ciudad: String, foto: String): Observable<any> {
    this.messageService.add('RegisterService: Login call');
    var usuario_id = 0;
    var obj = { usuario_id: usuario_id, first_name: first_name, last_name: last_name, email: email, pais: pais, ciudad: ciudad, foto: foto }
    this.httpClient.post(this.API_URL, JSON.stringify(obj), httpOptions).subscribe((data: Response) => {
      if (data[0].fields.length) {
        this.router.navigate(['/']);
        this.messageService.add('Usuario adicionado');
        this.messageService.authenticate(true);
      } else {
        this.messageService.add('Usuario o contraseña incorrectos');
        this.messageService.authenticate(false);
      }
    });
    return of(obj);
  }
  
}