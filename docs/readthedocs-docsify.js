READTHEDOCS_DATA = {
    "ad_free": false,
    "api_host": "http://devthedocs.org",
    "build_date": "$READTHEDOCS_BUILD_DATE",
    "builder": "$DOCTOOL_NAME",
    "canonical_url": "$READTHEDOCS_CANONICAL_URL",
    "commit": "$DOCTOOL_COMMIT",
    "docroot": "$DOCTOOL_DOCROOT",
    "language": "$READTHEDOCS_LANGUAGE",
    "page": "$DOCTOOL_PAGE",  // Can we define this dynamically via Javascript?
    "programming_language": "$READTHEDOCS_PROGRAMMING_LANGUAGE",
    "project": "$READTHEDOCS_PROJECT",
    "version": "$READTHEDOCS_VERSION",
    "source_suffix": "$DOCTOOL_SOURCE_SUFFIX",
    "theme": "$DOCTOOL_THEME",

    // These can be removed
    "user_analytics_code": null,
    "global_analytics_code": null,
    "proxied_api_host": "/_",
    "subprojects": null,

    // TODO: remove the following ones, they are just my own tests
    // NOTE: eventually, some of these settings should be enabled/disabled by the reader
    "build": {
        "id": 1111,
        "external_version": true,
    },
    "repository_url": "https://github.com/readthedocs/test-builds",  // This one could be retrieved from the API
    "features": {
        "docsearch_disabled": false,
        "docdiff": {
            "enabled": true,
        },
    },
};
