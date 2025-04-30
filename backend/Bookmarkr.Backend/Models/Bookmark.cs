using System.ComponentModel.DataAnnotations;

namespace Bookmarkr.Backend;

public class Bookmark
{
    public int Id { get; set; }

    [Required]
    public string Title { get; set; }

    [Required]
    public string Url { get; set; }

    public DateTime TimeCreated { get; set; }

    public DateTime TimeLastUpdated { get; set; }

    public Bookmark(string title, string url)
    {
        this.Title = title;
        this.Url = url;
    }
}