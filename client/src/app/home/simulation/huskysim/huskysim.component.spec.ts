import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HuskysimComponent } from './huskysim.component';

describe('HuskysimComponent', () => {
  let component: HuskysimComponent;
  let fixture: ComponentFixture<HuskysimComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HuskysimComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HuskysimComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
