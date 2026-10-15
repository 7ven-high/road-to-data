# Architecture (NordBank)

```
Sources (CSV / synthetic)  ->  Ingestion (04)  ->  Warehouse (03: Snowflake + dbt)
                                                   |-- staging -> marts
                                                   |
                          BI dashboards (02) <-----+
                          ML models (05)  <--------+
```

TODO: replace this sketch with a real diagram (draw.io / Mermaid) as you build.
