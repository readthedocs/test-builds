// This data should be outputed by the builder at build time
// (this is the contract builders has to follow to integrate with our features)
// TODO: trim this data and only keep the useful one.
// This variable comes from
// https://github.com/rtfd/readthedocs-sphinx-ext/blob/f1145b1819458643f442b21083b3397aeebc8e72/readthedocs_ext/_templates/readthedocs-insert.html.tmpl#L30
// https://github.com/rtfd/readthedocs-sphinx-ext/blob/f1145b1819458643f442b21083b3397aeebc8e72/readthedocs_ext/readthedocs.py#L141-L194
READTHEDOCS_DATA = {
    "ad_free": false,
    "api_host": "http://devthedocs.org",
    "build_date": "2023-03-01T20:47:52Z",
    "builder": "sphinx",
    "canonical_url": null,
    "commit": "70ff6770",
    "docroot": "/docs/",
    "features": {
        "docsearch_disabled": false
    },
    "global_analytics_code": null,
    "language": "en",
    "page": "index",
    "programming_language": "words",
    "project": "test-builds",
    "proxied_api_host": "/_",
    "source_suffix": ".rst",
    "subprojects": {},
    "theme": "sphinx_rtd_theme",
    "user_analytics_code": "UA-12341234-1",
    "version": "latest",

    // TODO: remove the following ones, they are just my own tests
    "build": {
        "id": 1111,
        "external_version": true,
    },
    "repository_url": "https://github.com/readthedocs/test-builds",  // This one could be retrieved from the API
    "features": {
        "docdiff": {
            "enabled": true,
        },
    },
};

/*

Explanation about what field is useful for.
Besides, I'm starting to propose a potential JavaScript object that builders will need to output.

READTHEDOCS_DATA = {
    // Mandatory
    // Footer HTML endpoint
    "theme": "",
    "docroot": "",
    "source_suffix": "",
    "page": "",
    "project": "",
    "version": "",

    // NOTE: we are sending "subproject=true" attribute to the footer API,
    // if the URL contains "/projects/" on it.
    // However, the server is not using that argument at all

    // NOTE: Currently used, but why?
    // Shouldn't be always "/_"?
    // What are the cases where this will be different
    // https://github.com/readthedocs/readthedocs.org/blob/e18b40f6fe7c2c058bbf681063c1c577b5e8e9d3/readthedocs/core/static-src/core/js/doc-embed/footer.js#L65
    "proxied_api_host": "",

    // Search API
    "language": "",

    // Global analytics (for Read the Docs)
    // NOTE: this is not mandatory
    "programming_language": "",
    "builder": "",
    "global_analytics_code": "",

    // User specific analytics (added via the project's setting)
    "user_analytics_code": "",

    // New attributes
    // Use an Object for each feature.
    // This will allow us to expand in the future if required.
    "features": {
        "search": {
            "enabled": true,
        },
        "banner": {
            "warning": {
                "enabled": true,
                "versioning": "semver",
            },
        },
        "analytics": {
            "enabled": true,
        },
        "docdiff": {
            "enabled": true,
        },

    },
};

*/
