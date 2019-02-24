import { Injectable } from '@angular/core';
import { Observable, of, pairs } from 'rxjs';
import { HttpClient, HttpHeaders, HttpParams} from '@angular/common/http';
import { MessageService } from '../message/message.service';
import { Router } from '@angular/router';



@Injectable({
  providedIn: 'root'
})

export class AuthService {

  API_URL = 'http://localhost:8000/api/';

  constructor(private messageService: MessageService,
    private httpClient: HttpClient,
    private router: Router) 
     { }


  logOut(): Boolean {
    this.messageService.add('RegisterService: Login call');
    var res = false;
    this.httpClient.get(this.API_URL + "logOut").subscribe((data: Response) => {
      res = data[0].fields.logOut
    });
    return res;
  }

  logIn(): Boolean {
    this.messageService.add('RegisterService: Login call');
    var res = false;
    this.httpClient.get(this.API_URL + "login").subscribe((data: Response) => {
      if(data[0].fields.length>1){
        res = true
      }
    });
    return res;
  }

  isAuthenticated(): number {
    this.messageService.add('RegisterService: Login call');
    var id = -1;
    this.httpClient.get(this.API_URL + "authenticated").subscribe((data: Response) => {
      console.log(data)
      id = data["id"];
      
    });
    return id;
  }


  getEmail(user_id: number) : String {
    let params = new HttpParams();
    let email: String[] =[];
    params = params.append('usuario_id', user_id.toString());
    this.httpClient.get(this.API_URL + "get_user_by_id", {params}).subscribe((data: Response) => {
      email.push(data[0].fields.email);
    });

    return email[0];
  }

}
