// Copyright 2023 Proyectos y Sistemas de Mantenimiento SL (eProsima).
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License\.

#include <fastddsspy_participants/visualizer/NetworkVisualizer.hpp>

namespace eprosima {
namespace spy {
namespace participants {

NetworkVisualizer::NetworkVisualizer(
        const std::shared_ptr<ddspipe::core::DiscoveryDatabase>& discovery_database) noexcept
    : discovery_database_(discovery_database)
{
    // Do nothing
}

void NetworkVisualizer::print_participants(
        std::ostream& target /* = std::cout */) const noexcept
{
    // TODO IMPORTANT
    target << "<participants> still in progress..." << std::endl;
}

void NetworkVisualizer::print_datareaders(
        std::ostream& target /* = std::cout */) const noexcept
{
    // TODO IMPORTANT
    target << "<datareaders> still in progress..." << std::endl;
}

void NetworkVisualizer::print_datawriters(
        std::ostream& target /* = std::cout */) const noexcept
{
    // TODO IMPORTANT
    target << "<datawriters> still in progress..." << std::endl;
}

void NetworkVisualizer::print_topics(
        std::ostream& target /* = std::cout */) const noexcept
{
    // TODO IMPORTANT
    target << "<topics> still in progress..." << std::endl;
}

void NetworkVisualizer::new_participant_info(const ParticipantInfo& info) noexcept
{
    // TODO IMPORTANT
}

} /* namespace participants */
} /* namespace spy */
} /* namespace eprosima */
