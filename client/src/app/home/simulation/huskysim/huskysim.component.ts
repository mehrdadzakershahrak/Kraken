import { Component, OnInit, DoCheck, EventEmitter, Input, HostListener, ViewChild, ElementRef, ViewContainerRef } from '@angular/core';
import { Overlay } from 'ngx-modialog';
import { Modal } from 'ngx-modialog/plugins/bootstrap';
import { User } from '../../../_models/index';
import { UserService } from '../../../_services/index';
import { RosService } from '../../../_services/index';
import { HideService } from '../../../_services/index';
import { appConfig } from '../../../app.config';

@Component({
  selector: 'app-huskysim',
  templateUrl: './huskysim.component.html',
  styleUrls: ['./huskysim.component.css']
})
export class HuskysimComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
