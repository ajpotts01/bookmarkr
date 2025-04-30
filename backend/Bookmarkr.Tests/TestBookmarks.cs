using Bookmarkr.Backend;

namespace Bookmarkr.Tests;

public class TestBookmarks
{
    [Fact]
    public void Validate_BookmarkCreation_InMemory()
    {
        const string BookmarkTitle = "Test bookmark";
        const string BookmarkUrl = "https://www.google.com";

        BookmarkInMemoryDb db = new BookmarkInMemoryDb();

        BookmarkCreateRequest newBookmark = new BookmarkCreateRequest(BookmarkTitle, BookmarkUrl);

        Bookmark got = db.CreateBookmark(newBookmark);
        List<Bookmark> gotBookmarks = db.GetBookmarks();

        Assert.Equal(BookmarkTitle, got.Title);
        Assert.Equal(BookmarkUrl, got.Url);
        Assert.Equal(1, got.Id);
        Assert.Single(gotBookmarks);
    }

    [Fact]
    public void Validate_BookmarkDeletion_InMemory()
    {
        List<(string, string)> bookmarksToCreate = new List<(string, string)>() 
        { 
            ("Test 1", "https://www.google.com"),
            ("Test 2", "https://www.bing.com")
        };

        BookmarkInMemoryDb db = new BookmarkInMemoryDb();

        int latestId = 0;

        foreach ((string Title, string Url) nextBookmark in bookmarksToCreate)
        {
            BookmarkCreateRequest nextRequest = new BookmarkCreateRequest(nextBookmark.Title, nextBookmark.Url);
            Bookmark created = db.CreateBookmark(nextRequest);
            latestId = created.Id;
        }

        bool deleted = db.DeleteBookmark(latestId);
        List<Bookmark> bookmarks = db.GetBookmarks();
        Bookmark got = bookmarks.First();

        Assert.True(deleted);
        Assert.Single(bookmarks);   
        Assert.Equal("https://www.google.com", got.Url);
        Assert.Equal("Test 1", got.Title);
        Assert.Equal(1, got.Id);     
    }
}
