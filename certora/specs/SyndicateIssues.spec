using MocksETH as sETHToken
using MockSlotSettlementRegistry as slotSettlementRegistry
using MockStakeHouseUniverse as stakeHouseUniverse

methods {
    //// Regular methods
    totalETHReceived() returns (uint256) envfree
    isKnotRegistered(bytes32) returns (bool) envfree

    //// Resolving external calls
	// stakeHouseUniverse
	stakeHouseKnotInfo(bytes32) returns (address,address,address,uint256,uint256,bool) => DISPATCHER(true)
    memberKnotToStakeHouse(bytes32) returns (address) => DISPATCHER(true) // not used directly by Syndicate
    // stakeHouseRegistry
    getMemberInfo(bytes32) returns (address,uint256,uint16,bool) => DISPATCHER(true) // not used directly by Syndicate
    // slotSettlementRegistry
	stakeHouseShareTokens(address) returns (address)  => DISPATCHER(true)
	slotSettlementRegistry.numberOfCollateralisedSlotOwnersForKnot(bytes32) returns (uint256) envfree
	currentSlashedAmountOfSLOTForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	numberOfCollateralisedSlotOwnersForKnot(bytes32) returns (uint256)  => DISPATCHER(true)
	getCollateralisedOwnerAtIndex(bytes32, uint256) returns (address) => DISPATCHER(true)
	totalUserCollateralisedSLOTBalanceForKnot(address, address, bytes32) returns (uint256) => DISPATCHER(true)
    // sETH
    sETHToken.balanceOf(address) returns (uint256) envfree
    // ERC20
    name()                                returns (string)  => DISPATCHER(true)
    symbol()                              returns (string)  => DISPATCHER(true)
    decimals()                            returns (string) envfree => DISPATCHER(true)
    totalSupply()                         returns (uint256) => DISPATCHER(true)
    balanceOf(address)                    returns (uint256) => DISPATCHER(true)
    allowance(address,address)            returns (uint)    => DISPATCHER(true)
    approve(address,uint256)              returns (bool)    => DISPATCHER(true)
    transfer(address,uint256)             returns (bool)    => DISPATCHER(true)
    transferFrom(address,address,uint256) returns (bool)    => DISPATCHER(true)

    //// Harnessing
    // harnessed variables
    accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32,address) returns (uint256) envfree
    totalETHProcessedPerCollateralizedKnot(bytes32) returns (uint256) envfree
    sETHStakedBalanceForKnot(bytes32,address) returns (uint256) envfree
    sETHTotalStakeForKnot(bytes32) returns (uint256) envfree
    // harnessed functions
    deRegisterKnots(bytes32) 
    deRegisterKnots(bytes32,bytes32)
    stake(bytes32,uint256,address)
    stake(bytes32,bytes32,uint256,uint256,address)
    unstake(address,address,bytes32,uint256)
    unstake(address,address,bytes32,bytes32,uint256,uint256)
    claimAsStaker(address,bytes32)
    claimAsStaker(address,bytes32,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32,bytes32)
    registerKnotsToSyndicate(bytes32)
    registerKnotsToSyndicate(bytes32,bytes32)
    addPriorityStakers(address)
    addPriorityStakers(address,address)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32)

    // added by neumo
    getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32) returns(uint256) envfree
    sETHUserClaimForKnot(bytes32, address) returns(uint256) envfree
    PRECISION() returns(uint256) envfree
    lastAccumulatedETHPerFreeFloatingShare(bytes32) returns(uint256) envfree
    owner() returns (address) envfree
    updatePriorityStakingBlock(uint256)
    accumulatedETHPerFreeFloatingShare() returns(uint256) envfree
    accumulatedETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    isNoLongerPartOfSyndicate(bytes32) returns (bool) envfree
    priorityStakingEndBlock() returns (uint256) envfree
    isPriorityStaker(address) returns (bool) envfree
    lastSeenETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    lastSeenETHPerFreeFloating() returns(uint256) envfree
    calculateETHForFreeFloatingOrCollateralizedHolders() returns(uint256) envfree
    calculateUnclaimedFreeFloatingETHShare(bytes32, address) returns(uint256) envfree
    previewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    getETHBalance(address) returns(uint256) envfree
    batchPreviewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    calculateNewAccumulatedETHPerFreeFloatingShare() returns (uint256) envfree
    batchPreviewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    previewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    getUnprocessedETHForAllFreeFloatingSlot() returns (uint256) envfree
    getUnprocessedETHForAllCollateralizedSlot() returns (uint256) envfree
    numberOfRegisteredKnots() returns (uint256) envfree
    totalFreeFloatingShares() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedSharePerKnot() returns (uint256) envfree
    totalClaimed() returns (uint256) envfree
    calculateCollateralizedETHOwedPerKnot() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedShare(uint256) returns (uint256) envfree
    updateAccruedETHPerShares()
    updateCollateralizedSlotOwnersAccruedETH(bytes32)
    isInitialized() returns(bool) envfree
}

/// We defined additional functions to get around the complexity of defining dynamic arrays in cvl. We filter them in 
/// normal rules and invariants as they serve no purpose.
definition notHarnessCall(method f) returns bool = 
    f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32).selector
    && f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32).selector
    && f.selector != deRegisterKnots(bytes32).selector
    && f.selector != deRegisterKnots(bytes32,bytes32).selector
    && f.selector != stake(bytes32,uint256,address).selector
    && f.selector != stake(bytes32,bytes32,uint256,uint256,address).selector
    && f.selector != unstake(address,address,bytes32,uint256).selector
    && f.selector != unstake(address,address,bytes32,bytes32,uint256,uint256).selector
    && f.selector != claimAsStaker(address,bytes32).selector
    && f.selector != claimAsStaker(address,bytes32,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32,bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32,bytes32).selector
    && f.selector != addPriorityStakers(address).selector
    && f.selector != addPriorityStakers(address,address).selector
    && f.selector != batchPreviewUnclaimedETHAsFreeFloatingStaker(address,bytes32).selector
    && f.selector != getETHBalance(address).selector
    && f.selector != calculateCollateralizedETHOwedPerKnot().selector
    && f.selector != calculateNewAccumulatedETHPerCollateralizedShare(uint256).selector
    && f.selector != getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32).selector
    && f.selector != isInitialized().selector
    && f.selector != initialize(address,uint256,address,bytes32).selector
    && f.selector != getETHBalance(address).selector;


/// Functions with onlyOwner modifier.
definition onlyOwnerFunctions(method f) returns bool = 
    f.selector == deRegisterKnots(bytes32[]).selector
    || f.selector == registerKnotsToSyndicate(bytes32[]).selector
    || f.selector == addPriorityStakers(address[]).selector
    || f.selector == updatePriorityStakingBlock(uint256).selector;


/// Functions that internally call _updateCollateralizedSlotOwnersLiabilitySnapshot.
definition callsToLiabilitySnapshot(method f) returns bool = 
    f.selector == claimAsCollateralizedSLOTOwner(address,bytes32[]).selector
    || f.selector == updateCollateralizedSlotOwnersAccruedETH(bytes32).selector
    || f.selector == batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32[]).selector
    || f.selector == deRegisterKnots(bytes32[]).selector;


/// Corrollary that can be used as requirement after sETH solvency is proven.
function sETHSolvencyCorrollary(address user1, address user2, bytes32 knot) returns bool {
    return sETHStakedBalanceForKnot(knot,user1) + sETHStakedBalanceForKnot(knot,user2) <= sETHTotalStakeForKnot(knot);
}

/*-------------------------------------------------
|                    Real bugs                     |
--------------------------------------------------*/

/**
 *  After any function call, if a knot is deregistered it should be stored in lastAccumulatedETHPerFreeFloatingShare
 *  the last accumulatedETHPerFreeFloatingShare
 *
 *  Summary: When a knot is deregistered the value snaphotted in lastAccumulatedETHPerFreeFloatingShare must be the updated value of accumulatedETHPerFreeFloatingShare.
 *      The prover fails in calls to updateCollateralizedSlotOwnersAccruedETH and batchUpdateCollateralizedSlotOwnersAccruedETH
 *          - lastAccumulatedETHPerFreeFloatingShare before calling the function is 0
 *          - lastAccumulatedETHPerFreeFloatingShare after call to the function is 1
 *          - which is different that accumulatedETHPerFreeFloatingShare (it's 22) after calling updateAccruedETHPerShares
 *  Expected behaviour: If lastAccumulatedETHPerFreeFloatingShare is populated, meaning the knot has been deregistered, it has to be with the updated value of accumulatedETHPerFreeFloatingShare, so any call to updateAccruedETHPerShares() after that should not change the value of accumulatedETHPerFreeFloatingShare.
 *  References: https://github.com/Certora/2023-01-blockswap-fv/blob/certora/contracts/syndicate/Syndicate.sol#L345-L357
 */
rule lastAccumulatedETHPerFreeFloatingShareMustAccountForAccruedETH(method f) filtered {
    f -> notHarnessCall(f)
}{

    env e;

    bytes32 blsPubKey;

    require isKnotRegistered(blsPubKey);
    require !isNoLongerPartOfSyndicate(blsPubKey);
    require lastAccumulatedETHPerFreeFloatingShare(blsPubKey) == 0;

    calldataarg args;
    f(e, args);

    require isNoLongerPartOfSyndicate(blsPubKey);

    updateAccruedETHPerShares(e);

    assert lastAccumulatedETHPerFreeFloatingShare(blsPubKey) == accumulatedETHPerFreeFloatingShare(), "Knot deregistered, but lastAccumulatedETHPerFreeFloatingShare has a wrong value";

}

/**
 * Check that if totalETHProcessedPerCollateralizedKnot was bigger than accruedEarningPerCollateralizedSlotOwnerOfKnot 
 * it still is after any call to functions that call _updateCollateralizedSlotOwnersLiabilitySnapshot.
 *      The prover fails in calls to claimAsCollateralizedSLOTOwner, batchUpdateCollateralizedSlotOwnersAccruedETH, updateCollateralizedSlotOwnersAccruedETH and deRegisterKnots
 *          - totalETHProcessedPerCollateralizedKnot before calling the function is 1
 *          - accruedEarningPerCollateralizedSlotOwnerOfKnot before calling the function is 1
 *          - so totalETHProcessedPerCollateralizedKnot >= accruedEarningPerCollateralizedSlotOwnerOfKnot
 *          - totalETHProcessedPerCollateralizedKnot after call to the function is 2
 *          - accruedEarningPerCollateralizedSlotOwnerOfKnot after call to the function is 0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab
 *          - totalETHProcessedPerCollateralizedKnot should be greater than or equal to accruedEarningPerCollateralizedSlotOwnerOfKnot but it's not
 *  Summary: The value of accruedEarningPerCollateralizedSlotOwnerOfKnot cannot increase more than the value of the rewards being distributed
 *  Expected behaviour: the value of increase of totalETHProcessedPerCollateralizedKnot after a call that calls _updateCollateralizedSlotOwnersLiabilitySnapshot must be greater or equal than the amount of increase of accrued rewards for a single user 
 *  References: https://github.com/Certora/2023-01-blockswap-fv/blob/certora/contracts/syndicate/Syndicate.sol#L545-L564
 */
rule checkChangeInTotalETHProcessedPerCollateralized(method f) filtered {
    f -> callsToLiabilitySnapshot(f)
}{

    env e;

    bytes32 blsPubKey;
    address account;


    require totalETHProcessedPerCollateralizedKnot(blsPubKey) >= accruedEarningPerCollateralizedSlotOwnerOfKnot(blsPubKey, account);

    uint256 totalETHProcessedPerCollateralizedBefore = totalETHProcessedPerCollateralizedKnot(blsPubKey);

    calldataarg args;
    f(e, args);

    assert 
        totalETHProcessedPerCollateralizedKnot(blsPubKey) >= accruedEarningPerCollateralizedSlotOwnerOfKnot(blsPubKey, account)
        , "totalETHProcessedPerCollateralizedKnot cannot be less than accruedEarningPerCollateralizedSlotOwnerOfKnot";

}

/**
 * Check that if numberOfCollateralisedSlotOwnersForKnot is zero, totalETHProcessedPerCollateralizedKnot. should not change
 *      The prover fails in calls to updateCollateralizedSlotOwnersAccruedETH, batchUpdateCollateralizedSlotOwnersAccruedETH, claimAsCollateralizedSLOTOwner and deRegisterKnots
 *          - totalETHProcessedPerCollateralizedKnot before calling the function is 3
 *          - totalETHProcessedPerCollateralizedKnot after call to the function is 22
 *          - The value before and after shoul be equal but it's not
 *  Summary: If numberOfCollateralisedSlotOwnersForKnot is equal to zero, the value of totalETHProcessedPerCollateralizedKnot should not change after any call.
 *  Expected behaviour: If no slot owners exist for a given knot, the value of ETH processed of a knot shouldn't change after any call of the contract. But in _updateCollateralizedSlotOwnersLiabilitySnapshot the value is updated accounting for all accrued rewards of the knot regarding of the number of owners.
 *  References: https://github.com/Certora/2023-01-blockswap-fv/blob/certora/contracts/syndicate/Syndicate.sol#L563-L564
 */
rule checkNumberOfCollateralisedSlotOwnersForKnotIsZeroNoChangeInTotal(method f) filtered {
    f -> notHarnessCall(f)
}{

    env e;

    bytes32 blsPubKey;

    require slotSettlementRegistry.numberOfCollateralisedSlotOwnersForKnot(blsPubKey) == 0;
    uint256 totalETHProcessedPerCollateralizedBefore = totalETHProcessedPerCollateralizedKnot(blsPubKey);

    calldataarg args;
    f(e, args);

    assert totalETHProcessedPerCollateralizedKnot(blsPubKey) == totalETHProcessedPerCollateralizedBefore;

}