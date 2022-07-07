#!/usr/bin/env bash
psql -U $POSTGRES_USER $POSTGRES_DB -c 'COPY orders(date_closed,zone,waiter,cashier,products,diners,date_opened,"table",total,id,payments) from "/data/data.csv" CSV HEADER;'