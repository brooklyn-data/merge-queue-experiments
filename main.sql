/* count monthly active users */

with users as (
    select
        user_id,
        min(date) as first_date,
        max(date) as last_date
    from
        `looker-private-demo.ecomm.users`
    group by
        1
    )

, user_actions as (
    select
        user_id,
        date,
        count(*) as actions
    from
        `looker-private-demo.ecomm.user_actions`
    group by
        1,2
    )

, final as (
    select
        u.user_id,
        u.first_date,
        u.last_date,
        a.actions
    from
        users u
    left join
        user_actions a
    on
        u.user_id = a.user_id
    where
        u.first_date >= '2019-01-01'
    and
        u.first_date <= '2019-12-31'
    and
        u.last_date >= '2019-01-01'
    and
        u.last_date <= '2019-12-31'
    qualify row_number() over (partition by u.user_id order by u.first_date) = 1
)

select count(*) as monthly_active_users