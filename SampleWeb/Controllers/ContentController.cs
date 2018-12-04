using System;
using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Options;
using SampleWeb.Models;

namespace SampleWeb.Controllers
{
    public class ContentController : Controller
    {
        private readonly Content contentSig;
        public ContentController(IOptions<Content> option)
        {
            contentSig = option.Value;
        }

        /// <summary>
        /// 首页显示
        /// </summary>
        /// <returns></returns>
        public IActionResult Index()
        {
            var contents = new List<Content>();
            for (int i = 1; i < 11; i++)
            {
                contents.Add(new Content { Id = i, title = $"{i}的标题", content = $"{i}的内容", status = 1, add_time = DateTime.Now.AddDays(-i) });
            }
            contents.Add(contentSig);
            return View(new ContentViewModel { Contents = contents });
        }
    }
}