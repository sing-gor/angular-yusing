import { TestBed } from '@angular/core/testing';

import { SiteHandlerService } from './site-handler.service';

describe('SiteHandlerService', () => {
  let service: SiteHandlerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SiteHandlerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
