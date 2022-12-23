const CAR_RATE: f64 = 221.;
const MIN_HOUR: f64 = 60.;

pub fn production_rate_per_hour(speed: u8) -> f64 {
    let success_rate = match speed {
        1..=4  => 1.,
        5..=8 => 0.9,
        9|10 => 0.77,
        _ => 0.0
    };

    CAR_RATE * (speed as f64) * success_rate
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    (production_rate_per_hour(speed) / MIN_HOUR) as u32
}
