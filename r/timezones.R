
time_str_utc <- "2017-01-01 00:00:00 UTC"
time_in_pst <- parsedate::parse_date(time_str_utc)  # returns POSIXct class object
print(time_in_pst)  # Returns "2016-12-31 16:00:00 PST"

# When TZ is explicitly set, TZ is honored in comparisons
time_in_utc <- as.POSIXct(time_str_utc, tz="UTC")
print(time_in_utc)  # Returns "2017-01-01 UTC"
print(time_in_utc - time_in_pst) # Returns 0 which means timezone was honored

# When TZ is not explicitly set, TZ is not honored in comparisons
# A default locale time is assigned when TZ is not explicitly set
time_supposedly_in_utc <- as.POSIXct(time_str_utc)
print(time_supposedly_in_utc)  # Returns "2017-01-01 PST"
print(time_supposedly_in_utc - time_in_pst) # Returns `8 hours` which means timezone was not honored