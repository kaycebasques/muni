cmake_minimum_required(VERSION 3.13)
include(pico-sdk/external/pico_sdk_import.cmake)
project(app_project C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

pico_sdk_init()
add_executable(app main.c)
pico_enable_stdio_usb(app 1)
pico_enable_stdio_uart(app 1)
pico_add_extra_outputs(app)
target_link_libraries(app pico_stdlib hardware_i2c)

add_executable(picow_tls_client_poll
        picow_tls_client.c
        tls_common.c
        )
target_compile_definitions(picow_tls_client_poll PRIVATE
        WIFI_SSID=\"${WIFI_SSID}\"
        WIFI_PASSWORD=\"${WIFI_PASSWORD}\"
        )
target_include_directories(picow_tls_client_poll PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
        )
target_link_libraries(picow_tls_client_poll
        pico_cyw43_arch_lwip_poll
        pico_lwip_mbedtls
        pico_mbedtls
        pico_stdlib
        hardware_i2c
        )
pico_enable_stdio_usb(picow_tls_client_poll 1)
pico_enable_stdio_uart(picow_tls_client_poll 0)
pico_add_extra_outputs(picow_tls_client_poll)

# Ignore warnings from lwip code
set_source_files_properties(
        ${PICO_LWIP_PATH}/src/apps/altcp_tls/altcp_tls_mbedtls.c
        PROPERTIES
        COMPILE_OPTIONS "-Wno-unused-result"
        )
