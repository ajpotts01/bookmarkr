namespace Bookmarkr.Backend;

public record BookmarkCreateRequest(
    string Title,
    string Url
);