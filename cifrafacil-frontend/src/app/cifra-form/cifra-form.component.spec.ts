import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CifraFormComponent } from './cifra-form.component';

describe('CifraFormComponent', () => {
  let component: CifraFormComponent;
  let fixture: ComponentFixture<CifraFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CifraFormComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CifraFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
