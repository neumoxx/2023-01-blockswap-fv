 certoraRun  certora/harnesses/SyndicateHarness.sol \
        certora/harnesses/MockStakeHouseUniverse.sol \
        certora/harnesses/MockStakeHouseRegistry.sol \
        certora/harnesses/MockSlotSettlementRegistry.sol \
        certora/harnesses/MocksETH.sol \
        --verify SyndicateHarness:certora/specs/SyndicateUnitTests2.spec \
        --cloud master \
        --optimistic_loop \
        --optimize 1 \
        --loop_iter 3 \
        $RULE \
        --rule_sanity \
        --settings -optimisticFallback=true \
        --packages @blockswaplab=node_modules/@blockswaplab @openzeppelin=node_modules/@openzeppelin \
        --msg "Syndicate $specFile $1 $2"
