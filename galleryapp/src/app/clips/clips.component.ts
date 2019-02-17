import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import {NgbModal, ModalDismissReasons} from '@ng-bootstrap/ng-bootstrap';

import { Clip } from '../services/clip/clip';
import { ClipService } from '../services/clip/clip.service';

@Component({
  selector: 'app-clips',
  templateUrl: './clips.component.html',
  styleUrls: ['./clips.component.css']
})
export class ClipsComponent implements OnInit {

  clips: Clip[];
  closeResult: string;

  constructor(
    private route: ActivatedRoute,
    private clipService: ClipService,
    private location: Location,
    private modalService: NgbModal
  ) {}

  ngOnInit(): void {
    this.getClips();
  }
   
  getClips(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.clipService.getClips(id)
      .subscribe(clips => this.clips = clips);
  }
  
  goBack(): void {
    this.location.back();
  }

  open(content) {
    this.modalService.open(content, {ariaLabelledBy: 'modal-basic-title'}).result.then((result) => {
      this.closeResult = `Closed with: ${result}`;
    }, (reason) => {
      this.closeResult = `Dismissed ${this.getDismissReason(reason)}`;
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return  `with: ${reason}`;
    }
  }
}