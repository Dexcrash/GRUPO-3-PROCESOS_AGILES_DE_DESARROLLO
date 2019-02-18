import { Injectable } from '@angular/core';
import { Observable, of, pairs } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { MessageService } from '../message/message.service';
import { Router } from '@angular/router';
import { CompileNgModuleMetadata } from '@angular/compiler';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};


@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  API_URL = 'https://proyecto-agiles-grupo-no3.herokuapp.com/api/signup';

  constructor(private messageService: MessageService,
    private httpClient: HttpClient,
    private router: Router) { }

  register(username: String, password: String, first_name: String, last_name: String, email: String, pais: String, ciudad: String, foto: String): Observable<any> {
    this.messageService.add('RegisterService: Login call');
    var obj = { username: username, password: password, first_name: first_name, last_name: last_name, email: email, pais: pais, ciudad: ciudad, foto: foto }
    this.httpClient.post(this.API_URL, JSON.stringify(obj), httpOptions).subscribe((data: Response) => {
      if (data[0].fields.username == username) {
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
