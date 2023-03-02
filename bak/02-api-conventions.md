# Access across multiple indices

This convention cannot be used in single document APIs:

- **_all**: For all indices
- **comma:** A separator between two indices
- **wildcard (*,-):** The asterisk character, `*`, is used to match any sequence of characters in the index name, excluding the index afterwards

# Common options

- Boolean values: false means the mentioned value is false; true means the value is true.
- Number values: A number is as a string on top of the native JSON number type.
- Time unit for duration: The supported time units are 
    - `d` for days, 
    - `h` for hours, 
    - `m` for minutes, 
    - `s` for seconds, 
    - `ms` for milliseconds, 
    - `micros` for microseconds, and 
    - `nanos` for nanoseconds.
- Byte size unit: The supported data units are 
    - `b` for bytes, 
    - `kb` for kilobytes, 
    - `mb` for megabytes, 
    - `gb` for gigabytes, 
    - `tb` for terabytes, and 
    - `pb` for petabytes.
- Distance unit: The supported distance units are 
    - mi for miles, 
    - yd for yards, 
    - ft for feet, 
    - in for inches, 
    - km for kilometers, 
    - m for meters, 
    - cm for centimeters, 
    - mm for millimeters, and 
    - nmi or NM for nautical miles.
- Unit-less quantities: If the value specified is large enough, we can use a quantity as a multiplier. For instance, 10m represents the value 10,000,000. The supported quantities are 
    - `k` for kilo, 
    - `m` for mega, 
    - `g` for giga, 
    - `t` for tera, and 
    - `p` for peta. 
- Human-readable output: Values can be converted to human-readable values, such as 1h for 1 hour and 1kb for 1,024 kilobytes. This option can be turned on by adding ?human=true to the query string. The default value is false.
- Pretty result: If you append ?pretty=true to the request URL, the JSON string in the response will be in pretty format.
- REST parameters: Follow the convention of using underscore delimiting.
- Content type: The type of content in the request body must be specified in the request header using the Content-Type key name. Check the reference as to whether the content type you use is supported. In all our POST/UPDATE/PATCH request examples, application/json is used.
- Request body in query string: If the client library does not accept a request body for non-POST requests, you can use the source query string parameter to pass the request body and specify the   parameter with a supported media type.
- Stack traces: If the `error_trace=true` request URL parameter is set, the error stack trace will be included in the response when an exception is raised.

# Date math in a formatted date value

In range queries or in date range aggregations, you can format date fields using date math.

- The date math expressions start with an anchor date (`now`, or a date string ending with a double vertical bar: ||), followed by one or more sub-expressions such as +1h, -1d, or /d.
- The supported time units are different from the time units for duration in the previously mentioned Common options bullet list. Where 
    - `y` is for years, 
    - `M` is for months, 
    - `w` is for weeks, 
    - `d` is for days, 
    - `h`, or H is for hours, 
    - `m` is for minutes, 
    - `s` is for seconds, 
    - `+` is for addition,
    - `-` is for subtraction, and
    - `/` is for rounding down to the nearest time unit. For example, this means that /d means rounding down to the nearest day.
- For the following discussion of these data parameters, assume that the current system time now is 2019.01.03 01:20:00, 
    - now+1h is 2019.01.03 02:20:00, 
    - now-1d is 2019.01.02 01:20:00, 
    - now/d is 2019.01.03 00:00:00, 
    - now/M is 2019.01.01 00:00:00, 
    - 2019.01.03 01:20:00||+1h is 2019.01.03 02:20:00, 
    - and so forth. 