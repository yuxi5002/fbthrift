/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <array>
#include <cstddef>
#include <thrift/lib/cpp/Thrift.h>

#include "thrift/compiler/test/fixtures/frozen-struct/gen-cpp2/module_types.h"

namespace some { namespace ns {

struct _EnumBEnumDataStorage {
  using type = EnumB;
  static constexpr const std::size_t size = 1;
  static constexpr const std::array<EnumB, 1> values = {{
    EnumB::EMPTY,
  }};
  static constexpr const std::array<folly::StringPiece, 1> names = {{
    "EMPTY",
  }};
};

}} // some::ns
namespace apache { namespace thrift {

template <> struct TEnumDataStorage< ::some::ns::EnumB> {
  using storage_type =  ::some::ns::_EnumBEnumDataStorage;
};

}} // apache::thrift

