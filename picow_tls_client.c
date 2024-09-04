/*
 * Copyright (c) 2023 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"

#define TLS_CLIENT_SERVER        "worldtimeapi.org"
#define TLS_CLIENT_HTTP_REQUEST  "GET /api/ip HTTP/1.1\r\n" \
                                 "Host: " TLS_CLIENT_SERVER "\r\n" \
                                 "Connection: close\r\n" \
                                 "\r\n"
#define TLS_CLIENT_TIMEOUT_SECS  15
#define TLS_CLIENT_CONNECT_TIMEOUT_MS 60000

extern bool run_tls_client_test(const uint8_t *cert, size_t cert_len, const char *server, const char *request, int timeout);

int main() {
    stdio_init_all();
    sleep_ms(3000);
    printf("hi\n");
    printf("wifi_ssid: %s\n", WIFI_SSID);
    printf("wifi_password: %s\n", WIFI_PASSWORD);
    sleep_ms(3000);
    if (cyw43_arch_init()) {
        printf("init fail\n");
        return 1;
    }
    sleep_ms(3000);
    cyw43_arch_enable_sta_mode();
    sleep_ms(3000);
    if (cyw43_arch_wifi_connect_timeout_ms(WIFI_SSID, WIFI_PASSWORD, CYW43_AUTH_WPA2_AES_PSK, TLS_CLIENT_CONNECT_TIMEOUT_MS)) {
        printf("connect fail\n");
        return 1;
    }
    sleep_ms(3000);
    bool pass = run_tls_client_test(NULL, 0, TLS_CLIENT_SERVER, TLS_CLIENT_HTTP_REQUEST, TLS_CLIENT_TIMEOUT_SECS);
    sleep_ms(3000);
    if (pass) {
        printf("test pass\n");
    } else {
        printf("test fail\n");
    }
    sleep_ms(3000);
    cyw43_arch_deinit();
    sleep_ms(3000);
    printf("bye\n");
    return pass ? 0 : 1;
}
