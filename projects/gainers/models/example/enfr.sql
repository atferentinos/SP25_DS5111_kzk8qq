{{ config(materialized='table') }}

SELECT EN,FR
FROM DATA_SCIENCE.KZK8QQ_RAW.NUMBERS
