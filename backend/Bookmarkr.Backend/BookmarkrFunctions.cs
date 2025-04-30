using System.Text.Json;
using System.Text.Json.Serialization;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Extensions;
using Microsoft.Extensions.Logging;

namespace Bookmarkr.Backend
{
    public class BookmarkrFunctions
    {
        static List<Bookmark> bookmarks = new List<Bookmark>();

        private readonly ILogger<BookmarkrFunctions> _logger;

        public BookmarkrFunctions(ILogger<BookmarkrFunctions> logger)
        {
            _logger = logger;
        }

        [Function("GetBookmarks")]
        public static IActionResult GetBookmarks(
            [HttpTrigger(AuthorizationLevel.Function, "get", Route = "bookmark")] HttpRequest req,
            ILogger log)
        {
            log.LogInformation("Getting bookmarks");        

            return new OkObjectResult(bookmarks);
        }

        [Function("GetBookmark")]
        public static IActionResult GetBookmark(
            [HttpTrigger(AuthorizationLevel.Function, "get", Route = "bookmark/{id}")] HttpRequest req,
            ILogger log, int id
        )
        {
            log.LogInformation($"Getting bookmark with ID {id}");

            var bookmark = bookmarks.FirstOrDefault<Bookmark>(b => b.Id == id);

            if (bookmark == null)
            {
                return new NotFoundResult();
            }

            return new OkObjectResult(bookmark);
        }
        
        [Function("CreateBookmark")]
        public static IActionResult CreateBookmark(
            [HttpTrigger(AuthorizationLevel.Function, "post", Route = "bookmark")] HttpRequest req,
            ILogger log
        )
        {
            try
            {
                string body = new StreamReader(req.Body).ReadToEnd();
                var input = JsonSerializer.Deserialize<Bookmark>(body);
            }
            catch (JsonException ex)
            {
                log.LogError($"Error deserializing JSON in create request: {ex.Message}");
                // Func doesn't have an HTTP 500 result object?
                return new StatusCodeResult(StatusCodes.Status500InternalServerError);
            }

            return new CreatedResult();
        }                        
    }
}
