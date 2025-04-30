using System.Text.Json.Serialization;

namespace Bookmarkr.Backend;

public record BookmarkUpdateResponse(
    [property: JsonPropertyName("title")] string Title,
    [property: JsonPropertyName("url")] string Url,
    [property: JsonPropertyName("id")] int Id
); // do I need last updated/created?