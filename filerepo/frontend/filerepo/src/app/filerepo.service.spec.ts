import { TestBed } from '@angular/core/testing';

import { FilerepoService } from './filerepo.service';

describe('FilerepoService', () => {
  let service: FilerepoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FilerepoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
