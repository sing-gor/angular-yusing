import { Component, OnInit } from '@angular/core';
import { BlogHandlerService } from 'src/app/services/blog-handler.service';
import { Title } from '@angular/platform-browser';
import { BlogDetail } from 'src/app/models/blog.type';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-blog-detail',
  templateUrl: './blog-detail.component.html',
  styleUrls: ['./blog-detail.component.less'],
})
export class BlogDetailComponent implements OnInit {
  results: BlogDetail;
  category = [];
  constructor(
    private blogService: BlogHandlerService,
    private titleService: Title,
    private route: ActivatedRoute
  ) {
    this.route.paramMap.subscribe((params) => {
      this.getBlogDetail(params.get('slug'));
    });
  }

  ngOnInit(): void {}

  getBlogDetail = (slug) => {
    this.blogService.getBlogDetail(slug).subscribe(
      (data) => {
        this.results = data;
        this.titleService.setTitle(data.blog.title + ' | Sing NoteBook');
        this.blogService.changeTagsMessage(data.blog.tags);
        this.category.push(data.blog.category);
        this.blogService.changeCategoriesMessage(this.category);
      },
      (error) => {
        console.log(error);
      }
    );
  };
}
