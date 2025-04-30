namespace Bookmarkr.Backend;

public class BookmarkInMemoryDb 
{
    private List<Bookmark> _bookmarks;

    public BookmarkInMemoryDb()
    {
        _bookmarks = new List<Bookmark>();
    }

    public List<Bookmark> GetBookmarks()
    {
        return _bookmarks;
    }

    public Bookmark CreateBookmark(BookmarkCreateRequest create)
    {
        int id = 1;

        if (_bookmarks.Count > 0)
        {
            id = _bookmarks.Select(b => b.Id).Max() + 1;
        }

        DateTime creationTime = DateTime.UtcNow;

        Bookmark newBookmark = new Bookmark(create.Title, create.Url);

        newBookmark.Id = id;
        newBookmark.TimeCreated = creationTime;
        newBookmark.TimeLastUpdated = creationTime;

        _bookmarks?.Add(newBookmark);
        return newBookmark;
    }

    public Bookmark? GetBookmark(int id)
    {
        Bookmark? bookmark = _bookmarks.FirstOrDefault<Bookmark>(b => b.Id == id);

        return bookmark;
    }

    public Bookmark? UpdateBookmark(int id, BookmarkUpdateRequest update)
    {
        Bookmark? bookmark = GetBookmark(id);

        if (bookmark == null)
        {
            return null;
        }

        bookmark.Title = update.Title;
        bookmark.Url = update.Url;
        bookmark.TimeLastUpdated = DateTime.UtcNow;

        return bookmark;
    }

    public bool DeleteBookmark(int id)
    {
        Bookmark? bookmark = GetBookmark(id);

        if (bookmark == null)
        {
            return false;
        }

        _bookmarks.Remove(bookmark);
        return true;
    }
}