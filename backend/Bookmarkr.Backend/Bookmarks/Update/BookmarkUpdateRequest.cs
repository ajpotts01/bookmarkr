namespace Bookmarkr.Backend;

public record BookmarkUpdateRequest(
    string Title,
    string Url
);